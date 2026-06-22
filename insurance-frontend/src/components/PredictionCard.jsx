export default function PredictionCard({ data }) {
  const confidence = (
    data.confidence * 100
  ).toFixed(1);

  return (
    <div className="prediction-card">
      <h2>{data.predicted_category}</h2>

      <p>
        Confidence : {confidence}%
      </p>

      <div className="progress">
        <div
          className="progress-fill"
          style={{
            width: `${confidence}%`,
          }}
        ></div>
      </div>
    </div>
  );
}