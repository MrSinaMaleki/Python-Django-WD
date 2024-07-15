/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        "cardbg": "#E4FDE1",
        "cardbgsmall": "#114B5F"
      },
      fontFamily: {
        "raleway":["Raleway",]
      }

    },
  },
  plugins: [],
}

