import { useState } from "react";
import { predictPrice } from "../services/api";

function Predict({ setPrediction }) {

  const [year, setYear] = useState("");
  const [usdRate, setUsdRate] = useState("");

  const handlePredict = async () => {
    try {
      const data = await predictPrice(year, usdRate);
  
      console.log(data);   // check response
  
      setPrediction(data.prediction);
  
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <h2 className="text-xl font-bold mb-4">
        Predict Gold Price
      </h2>
      <input
        type="number"
        placeholder="Year"
        className="border p-2 rounded w-full mb-3"
        value={year}
        onChange={(e) => setYear(e.target.value)}
      />
      <input
        type="number"
        placeholder="USD to INR rate"
        className="border p-2 rounded w-full mb-3"
        value={usdRate}
        onChange={(e) => setUsdRate(e.target.value)}
      />
      <button
        onClick={handlePredict}
        className="bg-yellow-500 text-white px-4 py-2 rounded"
      >
        Predict
      </button>
    </div>
  );
}

export default Predict;