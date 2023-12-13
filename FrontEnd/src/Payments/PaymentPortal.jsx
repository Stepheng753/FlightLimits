import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { DuffelPayments } from '@duffel/components';
import '../css/App.css';
import airplane from '../assets/airplane.gif';
import fetchImg from '../assets/fetch.gif';

function PaymentPortal() {
	const [buttonText, setButtonText] = useState('Fetch Token');
	const [duffelPmtElement, setDuffelPmtElement] = useState(<h4>No Payment Intent Client Token</h4>);
	const [tokenWaiting, setTokenWaiting] = useState(false);
	const [loadingImg, setLoadingImg] = useState(airplane);
	const [redirect, setRedirect] = useState({ to: '' });

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} />;
	}

	function fetchToken() {
		if (!tokenWaiting) {
			setDuffelPmtElement(<h4>No Payment Intent Client Token</h4>);
			setTokenWaiting(true);
			setButtonText('Fetching Payment Intent Client Token');
			setLoadingImg(fetchImg);

			fetch('/api/run', { method: 'GET' })
				.then((res) => res.json())
				.then((data) => {
					setDuffelPmtElement(
						<DuffelPayments
							paymentIntentClientToken={data.client_token}
							onSuccessfulPayment={console.log}
							onFailedPayment={console.log}
							debug={false}
						/>
					);
					setTokenWaiting(false);
					setButtonText('Fetch Token');
					setLoadingImg(airplane);

					console.log(data);
				});
		} else {
			console.log('Currently Fetching Payment Intent Client Token');
		}
	}

	return (
		<div>
			<div>
				<img
					src={loadingImg}
					className="logo airplane"
					alt="Flight Limits"
					onClick={() => setRedirect({ to: '/' })}
				/>
			</div>
			<h1>Payment Portal</h1>
			<br />
			<button onClick={() => fetchToken()}>
				<h3>{buttonText}</h3>
			</button>
			<br />
			<br />
			{duffelPmtElement}
		</div>
	);
}

export default PaymentPortal;
