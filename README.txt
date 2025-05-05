
# CBA API with Flask

## How to deploy on Render.com

1. Create a new Web Service on https://render.com/
2. Upload this folder or push it via GitHub
3. Set the build command to:
   pip install -r requirements.txt
4. Set the start command to:
   python app.py
5. Access your API at: https://your-service-name.onrender.com/cba

## Example POST request:

POST https://your-service-name.onrender.com/cba
Content-Type: application/json

{
  "A": {
    "CAPEX": [315000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "OPEX": [0, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000],
    "BENEFITS": [0, 266900, 266900, 266900, 266900, 266900, 266900, 266900, 266900, 266900, 266900]
  },
  "B": {...},
  "C": {...}
}
