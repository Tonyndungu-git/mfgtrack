# MFGTrack: Manufacturing Tracking App

## Still on going .......

MFGTrack is a comprehensive Manufacturing Tracking Application designed to streamline and optimize production processes for manufacturing businesses. It provides tools for managing suppliers, products, quality control, and packaging solutions.

## Features

- **Supplier Management**
  - Maintain a database of suppliers with contact details and address information.
  - View and manage supplier information easily.

- **Product Catalog**
  - Keep track of products, including names, descriptions, unit prices, and suppliers.
  - Add new products and update existing product information.

- **Quality Control**
  - Implement quality control measures to ensure product standards and compliance.
  - Track quality assurance processes and inspections.

- **Packaging Solutions**
  - Explore packaging options and manage packaging-related data.
  - Optimize packaging processes for efficiency.

## Key Components

- **Supplier Management**
  - Add new suppliers and update supplier information.
  - View a list of all suppliers and their details.

- **Product Management**
  - Add new products with detailed descriptions and pricing.
  - Associate products with specific suppliers.

- **Quality Control**
  - Define quality control processes and criteria.
  - Record quality inspection results and generate reports.

- **Packaging Management**
  - Explore different packaging options and materials.
  - Manage packaging requirements for different products.

## Installation and Setup

To run the MFGTrack application locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd mfgtrack_project
   ```

3. Install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application in your web browser at [http://localhost:8000/](http://localhost:8000/).

## Technologies Used

- Python
- Django
- HTML/CSS
- JavaScript
- Bootstrap

## Contributing

Contributions to the MFGTrack project are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).