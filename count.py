import sys 
import os

class Bunch(object):
    def __init__(self, adict):
        self.__dict__.update(adict)


        
default_parameters = dict(
IN_DIR = "/home/bioinfo/ShaliniR/pipeline/in_dir/",
OUT_DIR = "/home/bioinfo/ShaliniR/pipeline/out_dir/",
SAMPLE_LIST =['sample1', 'sample2','sample3'],

GENOME = "/data1/ngs/genomes/Homo_sapiens/UCSC/hg19/Sequence/BWAIndex/genome.fa",
BWAINDEX = "/data1/ngs/genomes/Homo_sapiens/UCSC/hg19/Sequence/Bowtie2Index/genome",
REF_GENES = "/data1/ngs/genomes/Homo_sapiens/UCSC/hg19/Annotation/Genes/genes.gtf",
miRNA_GTF = "/data1/ngs/genomes/Homo_sapiens/UCSC/hg19/Sequence/miRBASE/hsa.gff3",
TRIMMED_DATA ="/home/bioinfo/ShaliniR/pipeline",
GTF_LIST = "/home/bioinfo/ShaliniR/pipeline/assembly_GTF_list.txt",

BAM_FILE_NAME = "accepted_hits.bam",
RAW_DATA_DIR = "/home/bioinfo/ShaliniR/pipeline/RAW_DATA",
STAR_INDEX = "/home/bioinfo/ShaliniR/pipeline/star_genome",
STAR_OPTIONS = "--readFilesCommand cat --runThreadN 20 --outSAMstrandField intronMotif --outFilterIntronMotifs RemoveNoncanonical",  
STAR_RESULTS = "/home/bioinfo/ShaliniR/pipeline/STAR_alignments" 
HTSEQ_OPTIONS ="-m intersection-nonempty -s no -t exon"
HTSEQ_RESULTS = "/home/shalini/pipeline/HTSEQ_RESULTS"
) 

p = Bunch(default_parameters)

def fastqc():
	for sample in p.SAMPLE_LIST:
		cmd = "fastqc -o %s %s/%s.fastq" % (p.OUT_DIR, p.IN_DIR, sample)
		print cmd
		os.system(cmd)
	return

def star():
        for sample in p.SAMPLE_LIST:
                cmd = "STAR --genomeDir %s --readFilesIn %s/%s.fastq %s --outFileNamePrefix %s/%s" % (p.STAR_INDEX, p.RAW_DATA_DIR, sample, p.STAR_OPTIONS, p. STAR_RESULTS, sample)
                print cmd
                os.system(cmd)
        return

def htseq():
        for sample in p.SAMPLE_LIST:
                cmd = "samtools view %s/%s/%s | sort -s -k 1,1 - |  htseq-count %s - %s > %s/%s_counts.txt" % (p. STAR_RESULTS, sample, p. BAM_FILE_NAME, p. HTSEQ_OPTIONS, p. REF_GENES, p.HTSEQ_RESULTS, sample)
                print cmd
                os.system(cmd)
        return


if __name__ == '__main__':
	
#	fastqc()
	star()
#	htseq()
	
	sys.exit(0)
