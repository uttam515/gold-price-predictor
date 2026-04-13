import { useState } from "react";

import Predict from "./Predict";
import History from "./History";

function Dashboard() {

  const [prediction, setPrediction] = useState(null);

  return (
    <div className="p-6 space-y-10">

      <h1 className="text-3xl font-bold text-center text-yellow-600">
        Gold Price Predictor
      </h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-10">

        <div className="bg-white shadow rounded p-6">
          <Predict setPrediction={setPrediction} />
        </div>

        <div className="bg-white shadow rounded p-6">
          <History prediction={prediction} />
        </div>

      </div>

    </div>
  );
}

export default Dashboard;