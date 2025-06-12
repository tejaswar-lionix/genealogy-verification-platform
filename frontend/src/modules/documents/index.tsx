import React, {useState} from 'react';
export const DocumentsView: React.FC = () => {
  const [filter,setFilter]=useState('high');
  return <div><h2>DOCUMENTS - Documents - census 1790-1950, ship 1800-</h2><p>census 1790</p></div>
};
export default DocumentsView;
