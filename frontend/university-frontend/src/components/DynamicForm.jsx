import { useEffect, useState } from "react";
import { useParams, useNavigate } from "react-router-dom";
import API from "../api/api";

function DynamicForm() {
  const { universityId } = useParams();
  const [university, setUniversity] = useState(null);
  const navigate = useNavigate();

  const [fields, setFields] = useState([]);
  const [formData, setFormData] = useState({});
  const [files, setFiles] = useState({});

  useEffect(() => {
    API.get(`universities/${universityId}/fields/`)
      .then((res) => setFields(res.data))
      .catch((err) => console.error(err));
  }, [universityId]);

  useEffect(() => {
    API.get(`universities/${universityId}/`)
    .then(res => setUniversity(res.data))
    .catch(err => console.error(err));
  }, [universityId]);

  const handleChange = (fieldId, value) => {
    setFormData((prev) => ({
      ...prev,
      [`field_${fieldId}`]: value,
    }));
  };

  const handleFileChange = (fieldId, file) => {
    setFiles((prev) => ({
      ...prev,
      [`field_${fieldId}`]: file,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = new FormData();
    data.append("university_id", universityId);

    Object.entries(formData).forEach(([key, value]) => {
      data.append(key, value);
    });

    Object.entries(files).forEach(([key, file]) => {
      data.append(key, file);
    });

    try {
      await API.post("application/submit/", data);
      alert("Application submitted!");
      setFormData({});
      setFiles({});
    } catch (err) {
      alert(err.response?.data?.error || "Submission failed");
    }
  };

  return (
    <div className="page-wrapper">
      <div className="form-card">
        {university && (
          <div style={{ marginBottom: "20px" }}>
            <h2>{university.name}</h2>
            <p><strong>Location:</strong> {university.location}</p><br></br>
            <p><strong>Description:</strong>{university.description}</p>
          </div>
        )}
        <h2>Application Form</h2>
        <form onSubmit={handleSubmit}>
          {fields.map((field) => (
            <div className="form-group" key={field.id}>
              <label>{field.name}</label>

              {field.field_type === "text" && (
                <input
                  type="text"
                  required={field.is_required}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                />
              )}

              {field.field_type === "number" && (
                <input
                  type="number"
                  required={field.is_required}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                />
              )}

              {field.field_type === "date" && (
                <input
                  type="date"
                  required={field.is_required}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                />
              )}

              {field.field_type === "dropdown" && (
                <select
                  className="select"
                  required={field.is_required}
                  onChange={(e) => handleChange(field.id, e.target.value)}
                >
                  <option value="">Select</option>
                  {field.options?.map((opt, i) => (
                    <option key={i} value={opt}>
                    {opt}
                    </option>
                  ))}
                </select>
              )}

              {field.field_type === "file" && (
                <input
                  type="file"
                  required={field.is_required}
                  onChange={(e) =>
                    handleFileChange(field.id, e.target.files[0])
                  }
                />
              )}
            </div>
          ))}

          <button className="submit-btn" type="submit" onClick={handleSubmit}>
            Submit Application
          </button>
        </form>
      </div>
    </div>
  );
}

export default DynamicForm;
