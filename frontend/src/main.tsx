import { BrowserRouter, Routes, Route } from "react-router-dom";
import PropertyList from "./pages/PropertyList";
import PropertyDetail from "./pages/PropertyDetail";
import ReactDOM from "react-dom/client";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <BrowserRouter>
    <Routes>
      <Route path="/" element={<PropertyList />} />
      <Route path="/properties/:id" element={<PropertyDetail />} />
    </Routes>
  </BrowserRouter>
);
