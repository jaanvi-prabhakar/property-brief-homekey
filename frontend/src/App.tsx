import PropertyList from "./pages/PropertyList";
import PropertyDetail from "./pages/PropertyDetail";
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/" element={<PropertyList />} />
      <Route path="/properties/:id" element={<PropertyDetail />} />
    </Routes>
  );
}

export default App;
