import { useState } from 'react';
import ReactDOM from 'react-dom/client';

export default function ScriptForm() {
  const [inputs, setInputs] = useState({});
  const [downloadAvailable, setDownloadavailable] = useState(false);

  const handleChange = (event) => {
    const name = event.target.name;
    const value = event.target.value;
    setInputs(values => ({...values, [name]: value}));
  }

  function download(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    // the filename you want
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    window.URL.revokeObjectURL(url);
  }

  const generate = (event) => {
    event.preventDefault();

    let params = inputs;
    
    // Extract each of the python packages
    let cleanString = params.packages.trim();
    params.packages = [];
    const packagesArray = cleanString.split(",");
    packagesArray.forEach((pythonPackage) => {
      params.packages.push(pythonPackage);
    });
    
    console.log(params);

    // Send data to the backend via POST
    fetch('/generateFiles', {  // Enter your IP address here
      headers: {
        'Content-Type': 'application/json',
      },
      method: 'POST',
      mode: 'cors',
      body: JSON.stringify(params) // body data type must match "Content-Type" header
    })
    .then(
      setDownloadavailable(true)
    )
  }

  const downloadPyScript = () => {
    fetch('/getScript')
      .then(response => {
        response.blob().then(blob => download(blob, 'script.py'))
      })
  }

  const downloadDockerfile = () => {
    fetch('/getDockerfile')
      .then(response => {
        response.blob().then(blob => download(blob, 'Dockerfile'))
      })
  }

  const datasetDescriptionExample = 
  'All files contain 6 columns of data. The first 5 columns contain readings and the last column contains a label\n\n' +
  'X1,X2,X3,X4,X5,y\n' +
  '-0.14265382212909766,-2.1467761306990853,0.9606401443602053,-1.4748228684171314,-0.05514735083422361,-72.53655711256799\n' +
  '-1.234162261977265,-0.46465302007687237,0.8835478057373728,0.3691192444797022,-0.14761343686650272,12.020964040292995\n' +
  '0.33743061172322536,1.2991697083756304,1.238595511114979,1.7409565221543206,0.8998460171769515,102.69669882706005';

  return (
    <>
    <form style={{width: "95%"}} onSubmit={generate}>
      <div className="form-group row">
          <label className="col-sm-4" htmlFor="problem">ML Problem:</label>
          <select className="custom-select col-sm-8" id="problem" name="problem" onChange={handleChange} style={{fontSize: "20px"}}>
            <option defaultValue>Choose...</option>
            <option value="machine learning regression modeling">Regression Modeling</option>
            <option value="machine learning classification modeling">Classification Modeling</option>
            <option value="statistical description analysis">Statistical Description Analysis</option>
          </select>
          <small style={{fontSize: "18px"}} id="problemHelpBlock" className="form-text text-muted">
            Select the type of ML problem you would like to run
          </small>
      </div>
      <br/>
      <div className="form-group row">
        <label htmlFor="fileType" className="col-sm-4 col-form-label">File Type:</label>
        <div className="col-sm-8">
          <input type="text" className="form-control" id="fileType" name="fileType" placeholder="csv" onChange={handleChange}/>
        </div>
        <small style={{fontSize: "18px"}} id="fileTypeHelpBlock" className="form-text text-muted">What type of file is your data? (e.g. csv, matlab, excel, xml, etc.)</small>
      </div>
      <br/>
      <div className="form-group row">
        <label htmlFor="packages" className="col-sm-3">Included Python Packages:</label>
          <div className="col-sm-9">
            <input type="text" className="form-control" id="packages" name="packages" placeholder="first-package,second-package" onChange={handleChange}/>
          </div>
        <small style={{fontSize: "18px"}} id="fileTypeHelpBlock" className="form-text text-muted">
          Please write each python package you would like to include exactly as written separated by a comma
        </small>
      </div>
      <div className="form-group">
        <label htmlFor="datasetDescription">Data Description:</label>
        <textarea 
          className="form-control" 
          name="datasetDescription" 
          id="datasetDescription" 
          rows="4" 
          placeholder={datasetDescriptionExample} 
          onChange={handleChange}>
        </textarea>
        <small style={{fontSize: "18px"}} id="fileTypeHelpBlock" className="form-text text-muted">
          Please describe your data and optionally provide a short example of your dataset in the space above
        </small>
      </div>
      <div className="form-group row">
        <div className="col-sm-12">
          <button className="btn btn-primary" style={{width: "100%"}}>Generate</button>
        </div>
      </div>
    </form>
    <span style={{flexDirection: "row"}}>
      <button 
        className="btn btn-success" 
        disabled={!downloadAvailable}
        onClick={downloadPyScript}>
          Download script.py
      </button>
      
      <button 
        className="btn btn-success"
        disabled={!downloadAvailable} 
        onClick={downloadDockerfile}>
          Download Dockerfile
      </button>
    </span>
    </>
  )
}

// <form onSubmit={handleSubmit}>
//       <label>
//         Select the type of ML problem you would like to run
//         <select name="problem" value={inputs.problem} onChange={handleChange}>
//           <option value="regression">Regression Modeling</option>
//           <option value="classification">Classification Modeling</option>
//           <option value="description">Statistical Description Analysis</option>
//         </select>
//       </label>
//       <br/>
//       <label>What type of file is this? (e.g. csv, matlab, excel, xml, etc.):
//       <input 
//         type="text" 
//         name="fileType" 
//         value={inputs.fileType || ""} 
//         onChange={handleChange}
//       />
//       </label>
//       <br/>
//       <label>Are there specific python packages that you would like to include? 
//         Please write each package exactly as written separated by a comma with no whitespace between:
//       <input 
//         type="text" 
//         name="packages" 
//         value={inputs.packages || ""} 
//         onChange={handleChange}
//       />
//       </label>
//       <br/>
//       <label>Please describe your data and optionally provide a short example of your dataset below:
//         <br/>
//         <textarea 
//           value={inputs.datasetDescription}
//           name="datasetDescription" 
//           cols="50"
//           rows="10"
//           placeholder="All files contain 4 columns of data. The first three columns contain readings and the last column contains a label
          
//           sample data"></textarea>

//         </label>
//         <input type="submit" />
//     </form>