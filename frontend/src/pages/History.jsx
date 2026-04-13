import { useEffect, useState } from "react";
import { getGoldHistory } from "../services/api";

import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  Scatter
} from "recharts";

function History({ prediction }) {

  const [data, setData] = useState([]);

  useEffect(() => {
    getGoldHistory().then(setData);
  }, []);

  const predictionPoint = prediction
    ? [{ date: "Prediction", price: prediction }]
    : [];

  return (
    <div>

      <h2 className="text-xl font-bold mb-4">
        Gold Price Trend
      </h2>

      <LineChart width={500} height={300} data={data}>
        <CartesianGrid strokeDasharray="3 3" />

        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />

        <Line type="monotone" dataKey="price" stroke="#f59e0b" />

        <Scatter data={predictionPoint} fill="red" />

      </LineChart>

    </div>
  );
}

export default History;