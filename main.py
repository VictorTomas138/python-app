from PIL import Image
import streamlit as st
import io


uploaded_files = st.file_uploader(
    "Escoge los archivos",
    accept_multiple_files=True)

if len(uploaded_files) > 0:
    try:
        images = []
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            img = Image.open(
                io.BytesIO(bytes_data))
            img = img.convert('RGB')
            images.append(img)

        file_name = st.text_input(
            "Modifique el nombre del archivo:", "Archivo.pdf")

        images[0].save(
            file_name,
            save_all=True,
            append_images=images[1:]
        )

        with open(file_name, 'rb') as archivo:
            st.download_button(
                label='Descargar',
                file_name=file_name,
                data=archivo)
    except Exception as e:
        st.title('Error')
