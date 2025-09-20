import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eef5ff',
          100: '#d6e7ff',
          200: '#a7caff',
          300: '#78aeff',
          400: '#4a92ff',
          500: '#1c76ff',
          600: '#145cdb',
          700: '#0e46a8',
          800: '#093075',
          900: '#051c47',
        },
      },
    },
  },
  plugins: [],
}
export default config
