import pickle

from django.shortcuts import render, redirect
from django.http import HttpResponse
from PIL import Image

from huffman_coding.tree import HuffmanTree
from huffman_coding.helper_functions import get_key, read_and_get_from_file

from app.forms import GetImageForm, GetTextForm, GetDecompressTextForm, GetDecompressImageForm


def create_tree_and_save_files(huffman_tree_obj):
    huffman_tree_obj.create_tree()
    key = get_key()
    compressed_file_data = huffman_tree_obj.get_compressed_file(key=key)
    meta_data = compressed_file_data[0]
    bit_array = compressed_file_data[1]

    with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
              f'media\\metadata\\'
              f'{key}.dat', 'wb') as fp:
        pickle.dump(meta_data, fp)

    with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
              f'media\\compressed'
              f'\\{key}.bin', 'wb') as fp:
        fp.write(bit_array)
    return f'{key}.bin'


def home(request):
    return render(request, 'app/home.html')


def about(request):
    return render(request, 'app/about.html')


def text_view(request):
    return render(request, 'app/text.html')


def image_view(request):
    return render(request, 'app/image.html')


def download_compressed_file_view(request, file_name):
    with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
              f'media\\compressed'
              f'\\{file_name}', 'rb') as fp:
        response = HttpResponse(fp.read(),
                                content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment;filename=compressed.bin'
        return response


def download_text_file_view(request, file_name):
    with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
              f'media\\temp'
              f'\\{file_name}', 'rb') as fp:
        response = HttpResponse(fp.read(), content_type='text/rtf')
        response['Content-Disposition'] = 'attachment;filename=decompressed.txt'
        return response


def download_image_file_view(request, file_name):
    with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
              f'media\\temp'
              f'\\{file_name}', 'rb') as fp:
        response = HttpResponse(fp.read(), content_type='image/bmp')
        response['Content-Disposition'] = 'attachment;filename=decompressed.bmp'
        return response


def text_cmp_view(request):
    if request.method == 'POST':
        form = GetTextForm(request.POST, request.FILES)
        if form.is_valid():
            fp = request.FILES['text']
            text = fp.read()
            text = str(text, 'utf-8')

            huffman_tree = HuffmanTree(data=text)
            file_name = create_tree_and_save_files(huffman_tree)
            return redirect('download-compressed-file', file_name)
    else:
        form = GetTextForm()
    return render(request, 'app/text_cmp.html', {'form': form})


def image_cmp_view(request):
    if request.method == 'POST':
        form = GetImageForm(request.POST, request.FILES)
        if form.is_valid():
            fp = request.FILES['image']
            with open(
                    r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp.bmp',
                    'wb') as temp_fp:
                temp_fp.write(fp.read())
            huffman_tree = HuffmanTree(
                file_path=r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp.bmp',
                is_image=True)
            file_name = create_tree_and_save_files(huffman_tree)

            return redirect('download-compressed-file', file_name)

    else:
        form = GetImageForm()
    return render(request, 'app/image_cmp.html', {'form': form})


def text_dcmp_view(request):
    if request.method == 'POST':
        form = GetDecompressTextForm(request.POST, request.FILES)
        if form.is_valid():
            fh = request.FILES['decompress_text']
            with open(
                    r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp_b.bin',
                    'wb') as temp_fp:
                temp_fp.write(fh.read())
            compressed_file_data = read_and_get_from_file(file_path=r'E:\PROGRAMMING\DJango\\Pied Piper Final Version '
                                                                    r'!\\media\temp\temp_b.bin')
            key = compressed_file_data['key']
            encoded_data = compressed_file_data['encoded_data']
            meta_data_file_name = f'{key}.dat'
            with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
                      f'media\\metadata'
                      f'\\{meta_data_file_name}', 'rb') as fp:
                meta_data = pickle.load(fp)

            huffman_tree = HuffmanTree(elements_dict=meta_data, is_decompression=True)
            huffman_tree.decompress(encoded_file_data=encoded_data)
            decoded_data = huffman_tree.decoded_data
            with open(
                    r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp_t.txt',
                    'w') as temp_fp:
                temp_fp.write(decoded_data)
            return redirect('download-text-file', 'temp_t.txt')

    else:
        form = GetDecompressTextForm()
    return render(request, 'app/text_dcmp.html', {'form': form})


def image_dcmp_view(request):
    if request.method == 'POST':
        form = GetDecompressImageForm(request.POST, request.FILES)
        if form.is_valid():
            fh = request.FILES['decompress_image']
            with open(
                    r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp_b.bin',
                    'wb') as temp_fp:
                temp_fp.write(fh.read())
            compressed_file_data = read_and_get_from_file(
                file_path=r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp_b.bin')
            key = compressed_file_data['key']
            encoded_data = compressed_file_data['encoded_data']
            meta_data_file_name = f'{key}.dat'
            with open(f'E:\\PROGRAMMING\\DJango\\Pied Piper Final Version !\\'
                      f'media\\metadata'
                      f'\\{meta_data_file_name}', 'rb') as fp:
                meta_data = pickle.load(fp)

            huffman_tree = HuffmanTree(elements_dict=meta_data,
                                       is_decompression=True,
                                       is_image=True)
            huffman_tree.decompress(encoded_file_data=encoded_data)
            decoded_image_data = huffman_tree.decoded_data
            image_size = huffman_tree.image_size

            new_image = Image.new('RGB', size=image_size)
            new_image.putdata(decoded_image_data)
            image_path = r'E:\PROGRAMMING\DJango\Pied Piper Final Version !\media\temp\temp_i.bmp'
            new_image.save(image_path)

            return redirect('download-image-file', 'temp_i.bmp')

    else:
        form = GetDecompressImageForm()

    return render(request, 'app/image_dcmp.html', {'form': form})
