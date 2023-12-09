import { DuffelPayments } from '@duffel/components';
import pmt_intent_data from '../../../.payment_intent/pmt_intent.json';
import '../css/App.css';

function PaymentPortal() {
	return (
		<div>
			<h1>Payment Portal</h1>
			<br />
			<button onClick={() => console.log('run.py')}>
				<h3>run.py</h3>
			</button>
			<br />
			<br />
			<DuffelPayments
				paymentIntentClientToken={pmt_intent_data.client_token}
				onSuccessfulPayment={console.log}
				onFailedPayment={console.log}
				debug={true}
			/>
		</div>
	);
}

export default PaymentPortal;
