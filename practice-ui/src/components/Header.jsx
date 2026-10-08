import { useTranslation } from "react-i18next";

function Header() {
  const { t, i18n } = useTranslation();

  return (
    <header>
      <h2> Bilingual Blog</h2>

      <label>
        {t("language")}:{" "}
      </label>

      <select
        value={i18n.language}
        onChange={(e) => i18n.changeLanguage(e.target.value)}
      >
        <option value="en">{t("english")}</option>
        <option value="ta">{t("tamil")}</option>
      </select>

      <hr />
    </header>
  );
}

export default Header;