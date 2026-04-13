import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-yellow-500 text-white p-4 flex justify-between items-center">

      <h1 className="text-xl font-bold">
        Gold Predictor
      </h1>

      <div className="flex gap-6">
        <Link to="/" className="hover:underline">
          Predict
        </Link>

        <Link to="/history" className="hover:underline">
          History
        </Link>
      </div>

    </nav>
  );
}

export default Navbar;