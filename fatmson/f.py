import os

def run_python_code_from_file(file_name):
    try:
        # Programın çalıştığı dizini al
        current_directory = os.path.dirname(os.path.realpath(__file__))
        
        # Dosya yolunu oluştur
        file_path = os.path.join(current_directory, file_name)
        
        # Dosyayı aç ve içeriğini oku
        with open(file_path, 'r') as file:
            code_lines = file.readlines()
        
        # Kodu çalıştırırken her satırı saymak için bir sayaç (counter) kullan
        line_count = 0
        function_line_count=0
        in_function_block = False  # Bir fonksiyon bloğu içinde miyiz?
        current_indent = 0  # Mevcut girinti seviyesi
        function_block = []  # Fonksiyon bloğunu tutacak liste
        
        for line in code_lines:
            line_count += 1
            # Boş satırları ve yorum satırlarını atla
            if  line.strip().startswith("#"):
                continue
            
            
            # İf, class veya fonksiyon bloğu başlıyor mu kontrol et
            if line.strip().startswith(("if ", "class ", "def ","try ","with ")) and line.strip().endswith(":") and not in_function_block:
                in_function_block = True
                function_block = [line]
            elif in_function_block:
                function_line_count+=1
                function_block.append(line)
            elif not in_function_block:
                try:
                    exec(line)
                except SyntaxError as se:
                    if "expected an indented block" in str(se):
                        print(f"Sözdizimi Hatası: İf bloğu veya fonksiyon tanımı eksik (Satır {line_count})")
                        print("Sözdizimi hatası nedeniyle kod çalıştırılamadı. İf bloğu veya fonksiyon tanımını kontrol edin.")
                    else:
                        print(f"Özel Hata: {se} (Satır {line_count})")
                except SyntaxError as se:
                    print(f"Sözdizimi Hatası: {se} (Satır {se.lineno})")
                    print("Sözdizimi hatası nedeniyle kod çalıştırılamadı. Daha fazla bilgi için Python belgelerine başvurun.")
                except IndentationError as ie:
                    print(f"Girinti Hatası: {ie} (Satır {ie.lineno})")
                    print("Girinti hatası nedeniyle kod çalıştırılamadı. Girintileri kontrol edin.")
                except TypeError as te:
                    print(f"Veri Türü Hatası: {te} (Satır {te.lineno})")
                    print("Veri türü hatası nedeniyle kod çalıştırılamadı. Veri türlerini kontrol edin.")
                except NameError as ne:
                    print(f"Tanımsız Değişken Hatası: {ne}")
                    print("Tanımsız değişken hatası nedeniyle kod çalıştırılamadı. Değişkenleri tanımlayın veya adlarını düzeltin.")
                except IndexError as ie:
                    print(f"Dizin Hatası: {ie} ")
                    print("Dizin hatası nedeniyle kod çalıştırılamadı. Dizini kontrol edin.")
                except KeyError as ke:
                    print(f"Anahtar Hatası: {ke}")
                    print("Anahtar hatası nedeniyle kod çalıştırılamadı. Sözlük anahtarlarını kontrol edin.")
                except ValueError as ve:
                    print(f"Değer Hatası: {ve} ")
                    print("Değer hatası nedeniyle kod çalıştırılamadı. Beklenen değerleri kontrol edin.")
                except ZeroDivisionError as zde:
                    print(f"Sıfıra Bölme Hatası: {zde} ")
                    print("Sıfıra bölme hatası nedeniyle kod çalıştırılamadı. Sıfıra böleni kontrol edin.")
                except FileNotFoundError as fnfe:
                    print(f"Dosya Bulunamadı Hatası: {fnfe}")
                    print("Dosya bulunamadı hatası nedeniyle kod çalıştırılamadı. Dosya yolunu kontrol edin.")
                except ModuleNotFoundError as mnfe:
                    print(f"Modül Bulunamadı Hatası: {mnfe}")
                    print("Modül bulunamadı hatası nedeniyle kod çalıştırılamadı. Modül adını kontrol edin.")
                except AttributeError as ae:
                    print(f"Özellik Hatası: {ae}")
                    print("Özellik hatası nedeniyle kod çalıştırılamadı. Nesne özelliklerini kontrol edin.")
                except Exception as e:
                    print(f"Bilinmeyen bir hata oluştu: {e}")
    

                
            if line.strip() == "" and in_function_block:
                in_function_block = False
                function_content = "".join(function_block)
                try:
                    print("\n")
                    exec(function_content)
                    print("\n")

                except SyntaxError as se:
                    print(f"Sözdizimi Hatası: {se} (Satır {se.lineno})")
                    print("Sözdizimi hatası nedeniyle kod çalıştırılamadı. Daha fazla bilgi için Python belgelerine başvurun.")
                except IndentationError as ie:
                    print(f"Girinti Hatası: {ie} (Satır {ie.lineno})")
                    print("Girinti hatası nedeniyle kod çalıştırılamadı. Girintileri kontrol edin.")
                except TypeError as te:
                    print(f"Veri Türü Hatası: {te} (Satır {te.lineno})")
                    print("Veri türü hatası nedeniyle kod çalıştırılamadı. Veri türlerini kontrol edin.")
                except NameError as ne:
                    print(f"Tanımsız Değişken Hatası: {ne}")
                    print("Tanımsız değişken hatası nedeniyle kod çalıştırılamadı. Değişkenleri tanımlayın veya adlarını düzeltin.")
                except IndexError as ie:
                    print(f"Dizin Hatası: {ie} ")
                    print("Dizin hatası nedeniyle kod çalıştırılamadı. Dizini kontrol edin.")
                except KeyError as ke:
                    print(f"Anahtar Hatası: {ke}")
                    print("Anahtar hatası nedeniyle kod çalıştırılamadı. Sözlük anahtarlarını kontrol edin.")
                except ValueError as ve:
                    print(f"Değer Hatası: {ve} ")
                    print("Değer hatası nedeniyle kod çalıştırılamadı. Beklenen değerleri kontrol edin.")
                except ZeroDivisionError as zde:
                    print(f"Sıfıra Bölme Hatası: {zde} ")
                    print("Sıfıra bölme hatası nedeniyle kod çalıştırılamadı. Sıfıra böleni kontrol edin.")
                except FileNotFoundError as fnfe:
                    print(f"Dosya Bulunamadı Hatası: {fnfe}")
                    print("Dosya bulunamadı hatası nedeniyle kod çalıştırılamadı. Dosya yolunu kontrol edin.")
                except ModuleNotFoundError as mnfe:
                    print(f"Modül Bulunamadı Hatası: {mnfe}")
                    print("Modül bulunamadı hatası nedeniyle kod çalıştırılamadı. Modül adını kontrol edin.")
                except AttributeError as ae:
                    print(f"Özellik Hatası: {ae}")
                    print("Özellik hatası nedeniyle kod çalıştırılamadı. Nesne özelliklerini kontrol edin.")
                except Exception as e:
                    print(f"Bilinmeyen bir hata oluştu: {e}")
    
                function_block = []
                function_line_count=0

    except FileNotFoundError as fnfe:
        print(f"Dosya Bulunamadı Hatası: {fnfe})")
        # Hata durumunda ekrana yazdır
        print("Hata durumu: Dosya bulunamadı hatası oluştu.")
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu: {e}")

if __name__ == "__main__":
    # Çalıştırmak istediğiniz .txt dosyasının adını dışarıdan alın
    file_name = input("Çalıştırmak istediğiniz dosyayı uzantısıyla birlikte girin ")
    print("\n")

    run_python_code_from_file(file_name)
