import { useState } from "react";
import API from "../services/api";
import Loader from "./Loader";
import PredictionCard from "./PredictionCard";

export default function PredictionForm() {
  const [loading, setLoading] =
    useState(false);

  const [result, setResult] =
    useState(null);

  const [formData, setFormData] =
    useState({
      age: "",
      weight: "",
      height: "",
      income_lpa: "",
      smoker: false,
      city: "",
      occupation: "private_job",
    });

  const handleChange = (e) => {
    const { name, value, checked, type } =
      e.target;

    setFormData({
      ...formData,
      [name]:
        type === "checkbox"
          ? checked
          : value,
    });
  };

  const calculateBMI = () => {
    if (
      !formData.weight ||
      !formData.height
    )
      return 0;

    return (
      formData.weight /
      ((formData.height / 100) ** 2)
    ).toFixed(1);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);

      const res = await API.post(
        "/predict",
        {
          age: Number(formData.age),
          weight: Number(formData.weight),
          height: Number(formData.height),
          income_lpa: Number(
            formData.income_lpa
          ),
          smoker: formData.smoker,
          city: formData.city,
          occupation:
            formData.occupation,
        }
      );

      setResult(res.data);
    } catch (error) {
      alert("Prediction Failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="form-section">
      <div className="glass-card">
        <h2>
          Insurance Premium
          Predictor
        </h2>

        <div className="bmi-box">
          Current BMI:
          <span>
            {calculateBMI()}
          </span>
        </div>

        <form onSubmit={handleSubmit}>
          <input
            type="number"
            name="age"
            placeholder=" Enter Age between 1  to 120"
            onChange={handleChange}
            required
          />

          <input
            type="number"
            name="weight"
            placeholder="Weight (kg)"
            onChange={handleChange}
            required
          />

          <input
            type="number"
            name="height"
            placeholder="Height (cm)"
            onChange={handleChange}
            required
          />

          <input
            type="number"
            name="income_lpa"
            placeholder="Income (LPA)"
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="city"
            placeholder="City"
            onChange={handleChange}
            required
          />

          <select
            name="occupation"
            onChange={handleChange}
          >
            <option value="student">
              Student
            </option>
            <option value="private_job">
              Private Job
            </option>
            <option value="government_job">
              Government Job
            </option>
            <option value="business_owner">
              Business Owner
            </option>
            <option value="freelancer">
              Freelancer
            </option>
            <option value="retired">
              Retired
            </option>
            <option value="unemployed">
              Unemployed
            </option>
                </select>

          <label className="checkbox">
            <input
              type="checkbox"
              name="smoker"
              onChange={handleChange}
            />
            Smoker
          </label>

          <button type="submit">
            Predict Premium
          </button>
        </form>

        {loading && <Loader />}

        {result && (
          <PredictionCard
            data={result}
          />
        )}
      </div>
    </section>
  );
}