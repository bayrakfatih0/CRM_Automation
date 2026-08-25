# Temel Python imajını kullanıyoruz
FROM python:3.11-slim

# Çalışma dizinini ayarlıyoruz
WORKDIR /app

# Chrome ve WebDriver için gerekli sistem bağımlılıklarını kuruyoruz
RUN apt-get update && apt-get install -y wget unzip \
    chromium \
    chromium-driver

# Proje dosyalarını içeri kopyalıyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Tüm projeyi kopyalıyoruz
COPY . .

# Testi çalıştıran varsayılan komut (Headless çalışması gerektiğini unutma!)
CMD ["pytest", "tests/", "--html=report.html"]