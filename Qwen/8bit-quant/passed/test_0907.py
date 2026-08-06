import pytest
from src_0907 import task_func
import os
import zipfile
import shutil

def test_task_func_no_files():
    source_dir = 'test_source'
    target_dir = 'test_target'
    archive_name = 'test_archive.zip'
    
    try:
        archive_path = task_func(source_dir, target_dir, archive_name)
        assert os.path.exists(archive_path)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            assert len(archive.namelist()) == 0
    finally:
        shutil.rmtree(source_dir, ignore_errors=True)
        shutil.rmtree(target_dir, ignore_errors=True)

def test_task_func_with_processed_files():
    source_dir = 'test_source'
    target_dir = 'test_target'
    archive_name = 'test_archive.zip'
    
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    processed_file = os.path.join(source_dir, 'file1_processed.txt')
    open(processed_file, 'w').close()
    
    try:
        archive_path = task_func(source_dir, target_dir, archive_name)
        assert os.path.exists(archive_path)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            assert len(archive.namelist()) == 1
            assert 'file1_processed.txt' in archive.namelist()
        
        assert os.path.exists(os.path.join(target_dir, 'file1_processed.txt'))
        assert not os.path.exists(processed_file)
    finally:
        shutil.rmtree(source_dir, ignore_errors=True)
        shutil.rmtree(target_dir, ignore_errors=True)

def test_task_func_with_non_processed_files():
    source_dir = 'test_source'
    target_dir = 'test_target'
    archive_name = 'test_archive.zip'
    
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    non_processed_file = os.path.join(source_dir, 'file1.txt')
    open(non_processed_file, 'w').close()
    
    try:
        archive_path = task_func(source_dir, target_dir, archive_name)
        assert os.path.exists(archive_path)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            assert len(archive.namelist()) == 0
        
        assert not os.path.exists(os.path.join(target_dir, 'file1.txt'))
        assert os.path.exists(non_processed_file)
    finally:
        shutil.rmtree(source_dir, ignore_errors=True)
        shutil.rmtree(target_dir, ignore_errors=True)

def test_task_func_with_multiple_files():
    source_dir = 'test_source'
    target_dir = 'test_target'
    archive_name = 'test_archive.zip'
    
    os.makedirs(source_dir, exist_ok=True)
    os.makedirs(target_dir, exist_ok=True)
    
    processed_file1 = os.path.join(source_dir, 'file1_processed.txt')
    processed_file2 = os.path.join(source_dir, 'file2_processed.txt')
    open(processed_file1, 'w').close()
    open(processed_file2, 'w').close()
    
    try:
        archive_path = task_func(source_dir, target_dir, archive_name)
        assert os.path.exists(archive_path)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            assert len(archive.namelist()) == 2
            assert 'file1_processed.txt' in archive.namelist()
            assert 'file2_processed.txt' in archive.namelist()
        
        assert os.path.exists(os.path.join(target_dir, 'file1_processed.txt'))
        assert os.path.exists(os.path.join(target_dir, 'file2_processed.txt'))
        assert not os.path.exists(processed_file1)
        assert not os.path.exists(processed_file2)
    finally:
        shutil.rmtree(source_dir, ignore_errors=True)
        shutil.rmtree(target_dir, ignore_errors=True)