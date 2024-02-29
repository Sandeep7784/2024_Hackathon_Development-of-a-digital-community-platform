import React, { useEffect, useState } from "react";
import Header from "./Header";
import SearchResultCard from "./searchResultsCard"; // Assuming you have SearchResultCard component
import { useParams } from "react-router-dom";

// const SearchResults = () => {
//   const { keyword } = useParams();
//   const [searchResults, setSearchResults] = useState([]);

//   useEffect(() => {
//     const fetchSearchResults = async () => {
//       try {
//         const response = await fetch(`your_backend_api_endpoint/${keyword}`);
//         const data = await response.json();
//         setSearchResults(data);
//       } catch (error) {
//         console.error('Error fetching search results:', error);
//       }
//     };

//     fetchSearchResults();
//   }, [keyword]);

//   const handleSendRequest = (itemId) => {
//     console.log('Sending request for item:', itemId);
//     // Implement logic to send request for the specific item
//   };

//   return (
//     <React.Fragment>
//       <Header />
//       <div className="container mx-auto mt-8">
//         <h2 className="text-3xl font-semibold mb-4">Search Results for "{keyword}"</h2>
//         {searchResults.map((result) => (
//           <SearchResultCard
//             key={result.id}
//             title={result.title}
//             tasks={result.tasks}
//             town={result.town}
//             onSendRequest={() => handleSendRequest(result.id)}
//           />
//         ))}
//       </div>
//     </React.Fragment>
//   );
// };

const dummySearchResults = [
  {
    id: 1,
    title: "Dummy Result 1",
    tasks: "Task 1, Task 2, Task 3",
    town: "Town 1",
    onSendRequest: () => console.log("Sending request for Dummy Result 1"),
  },
  {
    id: 2,
    title: "Dummy Result 2",
    tasks: "Task 4, Task 5, Task 6",
    town: "Town 2",
    onSendRequest: () => console.log("Sending request for Dummy Result 2"),
  },
  {
    id: 3,
    title: "Dummy Result 3",
    tasks: "Task 7, Task 8, Task 9",
    town: "Town 3",
    onSendRequest: () => console.log("Sending request for Dummy Result 3"),
  },
  {
    id: 4,
    title: "Dummy Result 4",
    tasks: "Task 10, Task 11, Task 12",
    town: "Town 4",
    onSendRequest: () => console.log("Sending request for Dummy Result 4"),
  },
];

const SearchResults = ({ keyword }) => {
  // Assuming you receive keyword as a prop
  return (
    <React.Fragment>
      <Header />
      <div className="container mx-auto mt-8">
        <h2 className="text-3xl font-semibold mb-4">
          Search Results for your query
        </h2>
        {dummySearchResults.map((result) => (
          <SearchResultCard
            key={result.id}
            title={result.title}
            tasks={result.tasks}
            town={result.town}
            onSendRequest={() => handleSendRequest(result.id)}
          />
        ))}
      </div>
    </React.Fragment>
  );
};

export default SearchResults;
