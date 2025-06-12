import React, {useState} from 'react';
export const SearchView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>SEARCH - Search - persons, soundex, date range, p</h2><p>soundex</p></div>
};
export default SearchView;
