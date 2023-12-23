import { useState } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { Form, convertFormDataToJSON } from '../Globals/Form';
import '../css/master.css';
import airplane from '../assets/airplane.gif';

function PaymentPortal() {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const [passengerParams, setPassengerParams] = useState([
		{ label: 'First Name', type: 'text', value: 'Stephen' },
		{ label: 'Last Name', type: 'text', value: 'Giang' },
		{ label: 'Title', type: 'text', value: 'Mr' },
		{ label: 'Date of Birth', type: 'date', value: '2000-03-02' },
		{ label: 'Gender', type: 'text', value: 'M' },
		{ label: 'Phone Number', type: 'tel', value: '+18582165827' },
		{ label: 'Email', type: 'email', value: 'StephenG753@Gmail.com' },
	]);
	const location = useLocation();
	let flight = location.state.data;
	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function fetchOrderFlight() {
		fetch('/api/order_flight', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ ...convertFormDataToJSON(passengerParams), flight_id: flight.id }),
		})
			.then((res) => res.json())
			.then((data) => {
				console.log(data.order.id);
			});
	}

	return (
		<div>
			<img
				src={airplane}
				className="logo airplane"
				alt="Flight Limits"
				onClick={() => setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/' }))}
			/>
			<h1>Payment Portal</h1>
			<br />
			{Form(passengerParams, setPassengerParams)}
			<br />
			<button onClick={() => fetchOrderFlight()}>
				<h3>Place Order</h3>
			</button>
		</div>
	);
}

export default PaymentPortal;
