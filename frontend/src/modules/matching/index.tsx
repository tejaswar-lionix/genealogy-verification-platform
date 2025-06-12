import React, {useState} from 'react';
export const MatchingView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>MATCHING - Matching - probabilistic, Soundex, date </h2><p>Soundex</p></div>
};
export default MatchingView;
