const BASE_URL = "http://127.0.0.1:8000";

export async function getProperties() {
  const res = await fetch(`${BASE_URL}/properties`);
  return res.json();
}

export async function getPropertyBrief(id: string) {
  const res = await fetch(`${BASE_URL}/properties/${id}/brief`);
  return res.json();
}
