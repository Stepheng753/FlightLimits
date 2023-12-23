import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { Form, convertFormDataToJSON } from '../Globals/Form';
import '../css/master.css';
import airplane from '../assets/airplane.gif';

function SearchFlights(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const [searchParams, setSearchParams] = useState([
		{ label: 'Origin', type: 'text', value: 'SAN' },
		{ label: 'Destination', type: 'text', value: 'SEA' },
		{ label: 'Depart Date', type: 'date', value: '2024-01-01' },
		{ label: 'Return Date', type: 'date', value: '2024-01-15' },
		{ label: 'Number of Adults', type: 'number', value: 1, min: 0 },
		{ label: 'Number of Children', type: 'number', value: 0, min: 0 },
		{ label: 'Cabin', type: 'text', value: 'economy' },
	]);

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function fetchOffers() {
		fetch('/api/get_all_offers', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(convertFormDataToJSON(searchParams)),
		})
			.then((res) => res.json())
			.then((data) => {
				setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/flight-card', state: { data } }));
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
			<h1>Search Flights</h1>
			<br />
			{Form(searchParams, setSearchParams)}
			<br />
			<button onClick={() => fetchOffers()}>
				<h3>Fetch Offers</h3>
			</button>
			<br />
		</div>
	);
}

export default SearchFlights;
