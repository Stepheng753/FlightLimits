import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { DuffelPayments } from '@duffel/components';
import '../css/App.css';
import airplane from '../assets/airplane.png';

function PaymentPortal() {
	const [runPyText, setRunPyText] = useState('run.py');
	const [duffelPmtElement, setDuffelPmtElement] = useState(<h4>No Payment Intent Client Token</h4>);
	const [tokenWaiting, setTokenWaiting] = useState(false);
	const [redirect, setRedirect] = useState(false);

	if (redirect == true) {
		return <Navigate to={'/'} />;
	}

	function getToken() {
		if (!tokenWaiting) {
			setTokenWaiting(true);
			setRunPyText('Fetching Payment Intent Client Token');
			setDuffelPmtElement(<h4>No Payment Intent Client Token</h4>);
			fetch('/api/run')
				.then((res) => res.json())
				.then((data) => {
					console.log(data);
					setDuffelPmtElement(
						<DuffelPayments
							paymentIntentClientToken={data.client_token}
							onSuccessfulPayment={console.log}
							onFailedPayment={console.log}
							debug={false}
						/>
					);
					setRunPyText('run.py');
					setTokenWaiting(false);
				});
		} else {
			console.log('Currently Fetching Payment Intent Client Token');
		}
	}

	return (
		<div>
			<div>
				<img src={airplane} className="logo" alt="Flight Limits" onClick={() => setRedirect(!redirect)} />
			</div>
			<h1>Payment Portal</h1>
			<br />
			<button onClick={() => getToken()}>
				<h3>{runPyText}</h3>
			</button>
			<br />
			<br />
			{duffelPmtElement}
		</div>
	);
}

export default PaymentPortal;
