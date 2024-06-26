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
  const [searchResults, setSearchResults] = useState([]);
  const cookies = localStorage.getItem('imp_cookie');
  const query_value = localStorage.getItem('keyword');
  
  useEffect(() => {
    const fetchSearchResults = async () => {
      try {
        await fetch('http://127.0.0.1:8000/search/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({query: query_value, cookie: cookies})
        });
        const data = await response.json();

        // Convert object into an array of objects
        const resultsArray = Object.entries(data).map(([qid, [title, ...tasks]]) => ({
          qid,
          title,
          tasks: tasks.join(', '),
        }));
        
        setSearchResults(resultsArray);
      } catch (error) {
        console.error('Error fetching search results:', error);
      }
    };

    fetchSearchResults();
  }, []);

  return (
    <React.Fragment>
      <Header />
      <div className="container mx-auto mt-8">
        <h2 className="text-3xl font-semibold mb-4">
          Search Results for your query
        </h2>
        {dummySearchResults.map((result) => (
          <SearchResultCard
            key={result.qid}
            title={result.title}
            tasks={result.tasks}
          />
        ))}
      </div>
    </React.Fragment>
  );
};

export default SearchResults;
