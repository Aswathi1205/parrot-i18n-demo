import { useEffect, useState } from "react";

function App() {
  const [language, setLanguage] = useState("en");
  const [translations, setTranslations] = useState({});

  useEffect(() => {
    fetch(`/api/translation-export/?locale=${language}`)
      .then((response) => response.json())
      .then((data) => {
        setTranslations(data);
      });
  }, [language]);

  return (
    <div>
      <h1>Demo</h1>

      <label>Language: </label>

      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        <option value="en">English</option>
        <option value="ta">Tamil</option>
        <option value="hi">Hindi</option>
      </select>

      <hr />

      <h2>{translations.welcome || "Welcome"}</h2>

      <p>{translations.good_morning || "Good Morning"}</p>

      <button>{translations.login || "Login"}</button>

      <button>{translations.home || "Home"}</button>

      <button>{translations.settings || "Settings"}</button>
    </div>
  );
}

export default App;