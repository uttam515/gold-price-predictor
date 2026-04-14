import { useState } from "react";
import Predict from "./Predict";
import History from "./History";

function Dashboard() {

  const [prediction, setPrediction] = useState(null);

  return (
    <div>

      <Predict setPrediction={setPrediction} />

      <h2>Predicted Price: ₹{prediction}</h2>

      <History prediction={prediction} />

    </div>
  );
}

export default Dashboard;