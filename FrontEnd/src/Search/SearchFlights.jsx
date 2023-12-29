import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import { MainImage, Form, convertFormDataToJSON, fetch_post } from '../Globals/Globals';

function SearchFlights(props) {
	const [redirect, setRedirect] = useState({ to: '', state: {}, replace: false });
	const [searchParams, setSearchParams] = useState([
		{ label: 'Origin', type: 'text', value: 'SAN' },
		{ label: 'Destination', type: 'text', value: 'SEA' },
		{ label: 'Depart Date', type: 'date', value: '2024-01-01' },
		{ label: 'Return Date', type: 'date', value: '2024-01-15' },
		{ label: 'Number of Adults', type: 'number', value: 1, min: 0 },
		{ label: 'Number of Children', type: 'number', value: 1, min: 0 },
		{ label: 'Number of Infants', type: 'number', value: 1, min: 0 },
		{ label: 'Cabin', type: 'text', value: 'economy' },
	]);

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} state={redirect.state} replace={redirect.replace} />;
	}

	function fetchOffers() {
		let api_link = '/api/get_all_offers';
		let body = JSON.stringify(convertFormDataToJSON(searchParams));
		let afterFunc = (data) => {
			setRedirect((prevRedirect) => ({ ...prevRedirect, to: '/flight-cards', state: { data } }));
		};

		fetch_post(api_link, body, afterFunc);
	}

	return (
		<div>
			<MainImage redirectFunc={setRedirect} />
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
