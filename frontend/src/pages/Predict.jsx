import { useState } from "react";
import { predictPrice } from "../services/api";

function Predict({ setPrediction }) {

  const [date, setDate] = useState("");
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {

    try {
      setLoading(true);

      const data = await predictPrice(date);

      setPrediction(data.prediction);

    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>

      <h2 className="text-xl font-bold mb-4">
        Predict Gold Price
      </h2>

      <input
        type="date"
        className="border p-2 rounded w-full"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />

      <button
        onClick={handlePredict}
        className="bg-yellow-500 text-white px-4 py-2 rounded mt-4"
      >
        Predict
      </button>

      {loading && <p className="mt-2">Predicting...</p>}

    </div>
  );
}

export default Predict;