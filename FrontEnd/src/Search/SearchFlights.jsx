import { useState } from 'react';
import { Navigate } from 'react-router-dom';
import '../css/App.css';
import airplane from '../assets/airplane.gif';

function SearchFlights() {
	const [redirect, setRedirect] = useState({ to: '' });
	const [searchParams, setSearchParams] = useState({
		origin: 'SAN',
		destination: 'ANC',
		departDate: '2023-12-20',
		returnDate: '2023-12-30',
		numAdults: 1,
		numChilds: 0,
		cabin: 'economy',
	});

	if (redirect.to.length > 0) {
		return <Navigate to={redirect.to} />;
	}

	function fetchOffers() {
		fetch('/api/post_test', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify(searchParams),
		})
			.then((res) => res.json())
			.then((data) => console.log(data));
	}

	function form() {
		return (
			<form>
				<label>
					Origin:{' '}
					<input
						type="text"
						value={searchParams.origin}
						onChange={(e) => setSearchParams({ ...searchParams, origin: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Destination:{' '}
					<input
						type="text"
						value={searchParams.destination}
						onChange={(e) => setSearchParams({ ...searchParams, destination: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Depart Date:{' '}
					<input
						type="date"
						value={searchParams.departDate}
						onChange={(e) => setSearchParams({ ...searchParams, departDate: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Return Date:{' '}
					<input
						type="date"
						value={searchParams.returnDate}
						onChange={(e) => setSearchParams({ ...searchParams, returnDate: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Number of Adult Passengers:{' '}
					<input
						type="number"
						value={searchParams.numAdults}
						onChange={(e) => setSearchParams({ ...searchParams, numAdults: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Number of Child Passengers:{' '}
					<input
						type="number"
						value={searchParams.numChilds}
						onChange={(e) => setSearchParams({ ...searchParams, numChilds: e.target.value })}
					/>
				</label>
				<br />
				<label>
					Cabin:{' '}
					<input
						type="text"
						value={searchParams.cabin}
						onChange={(e) => setSearchParams({ ...searchParams, cabin: e.target.value })}
					/>
				</label>
				<br />
				<br />
			</form>
		);
	}

	return (
		<div>
			<div>
				<img
					src={airplane}
					className="logo airplane"
					alt="Flight Limits"
					onClick={() => setRedirect({ to: '/' })}
				/>
			</div>
			<h1>Search Flights</h1>
			<br />
			{form()}
			<button onClick={() => fetchOffers()}>
				<h3>Fetch Offers</h3>
			</button>
			<br />
		</div>
	);
}

export default SearchFlights;
