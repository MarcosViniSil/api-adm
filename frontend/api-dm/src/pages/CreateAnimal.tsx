import { useState } from "react";
import "../styles/createAnimal.css";
import ReactMarkdown from "react-markdown";
import { Toaster, toast } from "sonner";
import { createAnimal } from "../services/animal.service";
import { CreateAnimalModel } from "../models/characteristics";
import { useNavigate } from 'react-router-dom';




export default function CreateAnimal() {

const navigate = useNavigate();
  const [form, setForm] = useState({
    animal: {
      name: "",
      image_url: "",
      color: "",
      height: "",
      weight: "",
    },
    characteristics: {
      habitat: "",
      region: "",
      practice: "",
      habits: "",
      location: {
        latitude: 0,
        longitude: 0,
      },
      location_description: "",
    },
  });

  const [isFetching, setIsFetching] = useState(false);

  const sendSuccess = (message: string, toastId: number) => {
    toast.success(`${message}`, {
      style: {
        background: "#346E62",
        color: "#fff",
      },
      id: toastId,
    });
  };

  const sendError = (message: string, toastId: number) => {
    toast.error(`${message}`, {
      style: {
        background: "#8B0000",
        color: "#fff",
      },
      id: toastId,
    });
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>,
    section: "animal" | "characteristics",
  ) => {
    setForm({
      ...form,
      [section]: {
        ...form[section],
        [e.target.name]: e.target.value,
      },
    });
  };

  const handleLocationChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({
      ...form,
      characteristics: {
        ...form.characteristics,
        location: {
          ...form.characteristics.location,
          [e.target.name]: Number(e.target.value),
        },
      },
    });
  };

  const handleSubmit = async (e: React.SubmitEvent) => {
    e.preventDefault();
    try {
      if (isFetching) {
        return;
      }
      setIsFetching(true);
      let token:string = await createAnimal(createAnimalModel());
      console.log(token)

      sendSuccess("Animal criado com sucesso",-1)
      setTimeout(() => {
        navigate('/')
      },1500)
    } catch (err) {
      console.log(err);
      sendError(String(err),-1)
    }finally{
      setIsFetching(false)
    }
  };

  const createAnimalModel = () => {
    let animalModel:CreateAnimalModel = {
        animal: {
            name: form.animal.name,
            image_url: form.animal.image_url,
            color: form.animal.color,
            height: form.animal.height,
            weight: form.animal.weight,
        },
        characteristics: {
            habitat: form.characteristics.habitat,
            region: form.characteristics.region,
            practice: form.characteristics.practice,
            habits: form.characteristics.habits,
            location: {
                latitude: form.characteristics.location.latitude,
                longitude: form.characteristics.location.longitude,
            },
            location_description: form.characteristics.location_description,
        }
    }

    return animalModel
  }

  return (
    <div className="page-container">
        <Toaster position="top-right" />
      <form className="form-wrapper" onSubmit={handleSubmit}>
        <h2 className="form-title">Criar Animal</h2>

        <div className="form-section">
          <h3>Animal</h3>

          <div className="form-grid">
            <input
              placeholder="Nome"
              name="name"
              onChange={(e) => handleChange(e, "animal")}
            />

            <input
              placeholder="Cor"
              name="color"
              onChange={(e) => handleChange(e, "animal")}
            />

            <input
              placeholder="Altura"
              name="height"
              onChange={(e) => handleChange(e, "animal")}
            />

            <input
              placeholder="Peso"
              name="weight"
              onChange={(e) => handleChange(e, "animal")}
            />

            <input
              className="form-full"
              placeholder="URL da imagem"
              name="image_url"
              onChange={(e) => handleChange(e, "animal")}
            />
          </div>
          <style></style>
          <img
            src={form.animal.image_url}
            alt="preview imagem"
            className="image-preview"
          />
        </div>

        <div className="form-section">

          <div className="form-grid">
            <div className="form-section">
              <h3>Características</h3>

              <div className="form-grid">
                <input
                  placeholder="Habitat"
                  name="habitat"
                  onChange={(e) => handleChange(e, "characteristics")}
                />

                <input
                  placeholder="Região"
                  name="region"
                  onChange={(e) => handleChange(e, "characteristics")}
                />
              </div>

              <div className="markdown-field">
                <label>Prática (Markdown suportado)</label>

                <textarea
                  name="practice"
                  placeholder="Exemplo: **Caça em grupo** ou *atividade noturna*"
                  onChange={(e) => handleChange(e as any, "characteristics")}
                />

                <div className="markdown-preview">
                  <ReactMarkdown>{form.characteristics.practice}</ReactMarkdown>
                </div>
              </div>

              <div className="markdown-field">
                <label>Hábitos (Markdown suportado)</label>

                <textarea
                  name="habits"
                  placeholder="Exemplo: - Dorme durante o dia"
                  onChange={(e) => handleChange(e as any, "characteristics")}
                />

                <div className="markdown-preview">
                  <ReactMarkdown>{form.characteristics.habits}</ReactMarkdown>
                </div>
              </div>
            </div>
          </div>

          <h3 style={{ marginTop: 20 }}>Localização</h3>

          <div className="location-grid">
            <input
              type="number"
              min="-180" max="180" step="any"
              placeholder="Latitude"
              name="latitude"
              onChange={handleLocationChange}
            />

            <input
              type="number"
              min="-180" max="180" step="any"
              placeholder="Longitude"
              name="longitude"
              onChange={handleLocationChange}
            />
          </div>

          <div className="location-grid" style={{ marginTop: 12 }}>
            <input
              style={{ width: "100%" }}
              placeholder="Descrição da localização"
              name="location_description"
              onChange={(e) => handleChange(e, "characteristics")}
            />
          </div>
        </div>

        <button className="submit-button">Criar Animal</button>
      </form>
    </div>
  );
}
