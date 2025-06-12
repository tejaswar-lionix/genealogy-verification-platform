import React, {useState} from 'react';
export const ApiView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>API - API - REST for persons, documents, verif</h2><p>POST person</p></div>
};
export default ApiView;
