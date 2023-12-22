import { useState } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { DuffelPayments } from '@duffel/components';
import '../css/master.css';
import airplane from '../assets/airplane.gif';
import fetchImg from '../assets/fetch.gif';

function PaymentPortal() {
	const [buttonText, setButtonText] = useState('Order Flight');
	const [tokenWaiting, setTokenWaiting] = useState(false);
	const [loadingImg, setLoadingImg] = useState(airplane);
	const [passengerData, setPassengerData] = useState({
		firstName: 'Stephen',
		lastName: 'Giang',
		title: 'Mr',
		dob: '2000-03-02',
		gender: 'm',
		phoneNum: '+18582165827',
		email: 'StephenG753@gmail.com',
	});
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const location = useLocation();
	let flight = location.state.flight;

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function fetchToken() {
		if (!tokenWaiting) {
			setTokenWaiting(true);
			setButtonText('Fetching Payment Intent Client Token');
			setLoadingImg(fetchImg);

			fetch('/api/order_flight', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					flight_id: flight.id,
					firstName: passengerData.firstName,
					lastName: passengerData.lastName,
					title: passengerData.title,
					dob: passengerData.dob,
					gender: passengerData.gender,
					phoneNum: passengerData.phoneNum,
					email: passengerData.email,
				}),
			})
				.then((res) => res.json())
				.then((data) => {
					if (data.success) {
						setButtonText('Flight Ordered!: '.concat(data.order.id));
					} else {
						setButtonText(data.error);
					}
					setLoadingImg(airplane);
				});
		}
	}

	function form() {
		return (
			<form>
				<label>
					First Name:{' '}
					<input
						type="text"
						value={passengerData.firstName}
						onChange={(e) => setPassengerData({ ...passengerData, firstName: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Last Name:{' '}
					<input
						type="text"
						value={passengerData.lastName}
						onChange={(e) => setPassengerData({ ...passengerData, lastName: e.target.value })}
					/>
				</label>
				<br />
				<label>
					title:{' '}
					<input
						type="text"
						value={passengerData.title}
						onChange={(e) => setPassengerData({ ...passengerData, title: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Date of Birth:{' '}
					<input
						type="date"
						value={passengerData.dob}
						onChange={(e) => setPassengerData({ ...passengerData, dob: e.target.value })}
					/>
				</label>
				<br />
				<label>
					gender:{' '}
					<input
						type="text"
						value={passengerData.gender}
						onChange={(e) => setPassengerData({ ...passengerData, gender: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Phone Number:{' '}
					<input
						type="tel"
						value={passengerData.phoneNum}
						onChange={(e) => setPassengerData({ ...passengerData, phoneNum: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Email:{' '}
					<input
						type="email"
						value={passengerData.email}
						onChange={(e) => setPassengerData({ ...passengerData, email: e.target.value })}
					/>
				</label>
				<br />
				<br />
			</form>
		);
	}

	return (
		<div>
			<div>
				<img
					src={loadingImg}
					className="logo airplane"
					alt="Flight Limits"
					onClick={() => setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/' }))}
				/>
			</div>
			<h1>Payment Portal</h1>
			<br />
			{form()}
			<button onClick={() => fetchToken()}>
				<h3>{buttonText}</h3>
			</button>
		</div>
	);
}

export default PaymentPortal;
