import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import SearchFlights from './Search/SearchFlights';
import FlightCards from './Offers/FlightCards';
import PaymentPortal from './Payments/PaymentPortal';
import Success from './Payments/Success';
import './css/master.css';

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<div>
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/search-flights" element={<SearchFlights />} />
					<Route path="/flight-cards" element={<FlightCards />} />
					<Route path="/payment-portal" element={<PaymentPortal />} />
					<Route path="/success" element={<Success />} />
				</Routes>
			</Router>
		</div>
	</React.StrictMode>
);
