import { FaChartLine } from "react-icons/fa";

export default function Hero() {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>
          Smart Insurance Premium
          Prediction
        </h1>

        <p>
          Predict insurance premium category
          using Machine Learning.
        </p>

        <FaChartLine className="hero-icon" />
      </div>
    </section>
  );
}