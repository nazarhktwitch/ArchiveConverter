import os
import sys
import zipfile
import py7zr
import rarfile
import tarfile
import gzip
import bz2
import lzma
import patoolib
from pyunpack import Archive
import logging
from datetime import datetime

class ArchiveConverter:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.temp_dir = "temp_extracted"
        
        # Проверяем и создаем папку для логов
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # Настройка логирования с указанием пути для логов
        log_filename = f"logs/archive_converter_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[logging.FileHandler(log_filename), logging.StreamHandler()]
        )
        logging.info("Starting ArchiveConverter process")
        
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

    def extract_archive(self):
        """Extract the given archive to the temporary directory."""
        try:
            logging.info(f"Extracting archive: {self.input_path}")
            if self.input_path.endswith('.zip'):
                with zipfile.ZipFile(self.input_path, 'r') as zip_ref:
                    zip_ref.extractall(self.temp_dir)
                    logging.info(f"Extracted {len(zip_ref.namelist())} files from ZIP archive")
            elif self.input_path.endswith('.rar'):
                with rarfile.RarFile(self.input_path) as rar_ref:
                    rar_ref.extractall(self.temp_dir)
                    logging.info(f"Extracted {len(rar_ref.infolist())} files from RAR archive")
            elif self.input_path.endswith('.7z'):
                with py7zr.SevenZipFile(self.input_path, mode='r') as z:
                    z.extractall(self.temp_dir)
                    logging.info(f"Extracted files from 7z archive: {z.getnames()}")
            elif self.input_path.endswith('.tar'):
                with tarfile.open(self.input_path, 'r') as tar_ref:
                    tar_ref.extractall(self.temp_dir)
                    logging.info(f"Extracted {len(tar_ref.getnames())} files from TAR archive")
            elif self.input_path.endswith('.gz'):
                with gzip.open(self.input_path, 'rb') as gz_ref:
                    with open(os.path.join(self.temp_dir, os.path.basename(self.input_path).replace('.gz', '')), 'wb') as f:
                        f.write(gz_ref.read())
                    logging.info(f"Extracted {os.path.basename(self.input_path)} from GZ archive")
            elif self.input_path.endswith('.bz2'):
                with bz2.open(self.input_path, 'rb') as bz2_ref:
                    with open(os.path.join(self.temp_dir, os.path.basename(self.input_path).replace('.bz2', '')), 'wb') as f:
                        f.write(bz2_ref.read())
                    logging.info(f"Extracted {os.path.basename(self.input_path)} from BZ2 archive")
            elif self.input_path.endswith('.xz'):
                with lzma.open(self.input_path, 'rb') as xz_ref:
                    with open(os.path.join(self.temp_dir, os.path.basename(self.input_path).replace('.xz', '')), 'wb') as f:
                        f.write(xz_ref.read())
                    logging.info(f"Extracted {os.path.basename(self.input_path)} from XZ archive")
            elif self.input_path.endswith('.arj') or self.input_path.endswith('.lzh'):
                Archive(self.input_path).extractall(self.temp_dir)
                logging.info(f"Extracted files from ARJ/LZH archive")
            else:
                # Поддерживаемые форматы для вывода
                supported_formats = ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.arj', '.lzh']
                logging.error(f"Unsupported archive format: {self.input_path}. Supported formats are: {', '.join(supported_formats)}")
                sys.exit(1)
            logging.info(f"Extraction completed: {self.input_path}")
        except Exception as e:
            logging.error(f"Error extracting the archive: {e}")
            sys.exit(1)

    def create_archive(self):
        """Create the output archive from the extracted files."""
        try:
            logging.info(f"Creating archive: {self.output_path}")
            if self.output_path.endswith('.zip'):
                with zipfile.ZipFile(self.output_path, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
                    for foldername, subfolders, filenames in os.walk(self.temp_dir):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            zip_ref.write(file_path, os.path.relpath(file_path, self.temp_dir))
                            logging.debug(f"Added file {file_path} to ZIP archive")
            elif self.output_path.endswith('.rar'):
                patoolib.create_archive(self.output_path, [self.temp_dir])
                logging.info(f"Created RAR archive: {self.output_path}")
            elif self.output_path.endswith('.7z'):
                with py7zr.SevenZipFile(self.output_path, mode='w') as z:
                    z.writeall(self.temp_dir, os.path.basename(self.temp_dir))
                    logging.info(f"Created 7z archive: {self.output_path}")
            elif self.output_path.endswith('.tar'):
                with tarfile.open(self.output_path, 'w') as tar_ref:
                    for foldername, subfolders, filenames in os.walk(self.temp_dir):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            tar_ref.add(file_path, os.path.relpath(file_path, self.temp_dir))
                            logging.debug(f"Added file {file_path} to TAR archive")
            elif self.output_path.endswith('.gz'):
                with open(self.output_path, 'wb') as gz_ref:
                    with gzip.GzipFile(fileobj=gz_ref, mode='wb') as f_out:
                        for foldername, subfolders, filenames in os.walk(self.temp_dir):
                            for filename in filenames:
                                file_path = os.path.join(foldername, filename)
                                with open(file_path, 'rb') as f_in:
                                    f_out.write(f_in.read())
                                logging.debug(f"Added file {file_path} to GZ archive")
            elif self.output_path.endswith('.bz2'):
                with open(self.output_path, 'wb') as bz2_ref:
                    with bz2.BZ2File(bz2_ref, 'wb') as f_out:
                        for foldername, subfolders, filenames in os.walk(self.temp_dir):
                            for filename in filenames:
                                file_path = os.path.join(foldername, filename)
                                with open(file_path, 'rb') as f_in:
                                    f_out.write(f_in.read())
                                logging.debug(f"Added file {file_path} to BZ2 archive")
            elif self.output_path.endswith('.xz'):
                with open(self.output_path, 'wb') as xz_ref:
                    with lzma.LZMAFile(xz_ref, 'wb') as f_out:
                        for foldername, subfolders, filenames in os.walk(self.temp_dir):
                            for filename in filenames:
                                file_path = os.path.join(foldername, filename)
                                with open(file_path, 'rb') as f_in:
                                    f_out.write(f_in.read())
                                logging.debug(f"Added file {file_path} to XZ archive")
            else:
                raise ValueError(f"Unsupported format for creating archive: {self.output_path}")
            logging.info(f"Archive created successfully: {self.output_path}")
        except Exception as e:
            logging.error(f"Error creating the archive: {e}")
            sys.exit(1)

    def clean_up(self):
        """Remove the temporary directory after conversion."""
        logging.info(f"Cleaning up temporary files in: {self.temp_dir}")
        for root, dirs, files in os.walk(self.temp_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
                logging.debug(f"Removed file: {os.path.join(root, name)}")
            for name in dirs:
                os.rmdir(os.path.join(root, name))
                logging.debug(f"Removed directory: {os.path.join(root, name)}")
        os.rmdir(self.temp_dir)
        logging.info("Temporary files cleaned up")

    def convert(self):
        """Extract the input archive and create the output archive."""
        logging.info("Starting conversion process")
        self.extract_archive()
        self.create_archive()
        logging.info(f"Archive successfully converted to {self.output_path}")
        self.clean_up()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        logging.error("Usage: python archive_converter.py <input_archive> <output_archive>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    converter = ArchiveConverter(input_path, output_path)
    converter.convert()
