import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import PaymentPortal from './Payments/PaymentPortal';

function App() {
	return (
		<div>
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/payment-portal" element={<PaymentPortal />} />
				</Routes>
			</Router>
		</div>
	);
}

export default App;
