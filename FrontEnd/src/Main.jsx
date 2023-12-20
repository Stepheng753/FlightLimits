import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './Home';
import PaymentPortal from './Payments/PaymentPortal';
import SearchFlights from './Search/SearchFlights';
import FlightCard from './Search/FlightCard';
import './css/master.css';

ReactDOM.createRoot(document.getElementById('root')).render(
	<React.StrictMode>
		<div>
			<Router>
				<Routes>
					<Route path="/" element={<Home />} />
					<Route path="/payment-portal" element={<PaymentPortal />} />
					<Route path="/search-flights" element={<SearchFlights />} />
					<Route path="/flight-card" element={<FlightCard />} />
				</Routes>
			</Router>
		</div>
	</React.StrictMode>
);
