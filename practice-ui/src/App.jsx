import { Routes, Route } from "react-router-dom";
import BlogList from "./pages/BlogList";
import BlogDetail from "./pages/BlogDetail";
import Header from "./components/Header";

function App() {
  return (
    <>
      <Header />

      <Routes>
        <Route path="/" element={<BlogList />} />
        <Route path="/posts/:id" element={<BlogDetail />} />
      </Routes>
    </>
  );
}

export default App;