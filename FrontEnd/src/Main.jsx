import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import PaymentPortal from './Payments/PaymentPortal';
import SearchFlights from './Search/SearchFlights';
import './css/index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<div>
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/payment-portal" element={<PaymentPortal />} />
					<Route path="/search-flights" element={<SearchFlights />} />
				</Routes>
			</Router>
		</div>
	</React.StrictMode>
);
