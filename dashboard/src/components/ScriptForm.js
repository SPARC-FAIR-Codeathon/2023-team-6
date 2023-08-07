import { useState } from 'react';
import ReactDOM from 'react-dom/client';

export default function ScriptForm() {
  const [inputs, setInputs] = useState({});

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}));
    console.log(inputs);
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    alert(inputs);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Select the type of ML problem you would like to run
        <select name="problem" value={inputs.problem} onChange={handleChange}>
          <option value="regression">Regression Modeling</option>
          <option value="classification">Classification Modeling</option>
          <option value="description">Statistical Description Analysis</option>
        </select>
      </label>
      <br/>
      <label>What type of file is this? (e.g. csv, matlab, excel, xml, etc.):
      <input 
        type="text" 
        name="fileType" 
        value={inputs.fileType || ""} 
        onChange={handleChange}
      />
      </label>
      <br/>
      <label>Are there specific python packages that you would like to include? 
        Please write each package exactly as written separated by a comma with no whitespace between:
      <input 
        type="text" 
        name="packages" 
        value={inputs.packages || ""} 
        onChange={handleChange}
      />
      </label>
      <br/>
      <label>Please describe your data and optionally provide a short example of your dataset below:
        <br/>
        <textarea 
          value={inputs.datasetDescription}
          name="datasetDescription" 
          cols="50"
          rows="10"
          placeholder="All files contain 4 columns of data. The first three columns contain readings and the last column contains a label
          
          sample data"></textarea>

        </label>
        <input type="submit" />
    </form>
  )
}
