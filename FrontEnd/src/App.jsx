import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import BoilerPlate from './BoilerPlate';
import PaymentPortal from './Payments/PaymentPortal';

function App() {
	return (
		<div>
			<Router>
				<Routes>
					<Route path="/" element={<BoilerPlate />} />
					<Route path="/payment-portal" element={<PaymentPortal />} />
				</Routes>
			</Router>
		</div>
	);
}

export default App;
