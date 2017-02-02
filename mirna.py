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
CUFFDIFF_INPUT_LIST_COND1 = "/home/bioinfo/ShaliniR/pipeline/TOPHAT_RESULTS/sample1/accepted_hits.bam, /home/bioinfo/ShaliniR/pipeline/TOPHAT_RESULTS/sample2/accepted_hits.bam",
CUFFDIFF_INPUT_LIST_COND2 = "/home/bioinfo/ShaliniR/pipeline/TOPHAT_RESULTS/sample3/accepted_hits.bam",

TOPHAT_OPTIONS = "-a 5 --microexon-search --library-type fr-secondstrand --no-discordant",
CUFFDIFF_OPTIONS= "-p 8 -FDR 0.01 -L Normal,OA,XY -N --compatible-hits-norm",

TOPHAT_RESULTS ="/home/bioinfo/ShaliniR/pipeline/TOPHAT_RESULTS",
CUFFLINKS_RESULTS = "/home/bioinfo/ShaliniR/pipeline/assemblies",
CUFFDIFF_RESULTS = "/home/bioinfo/ShaliniR/pipeline/CUFFDIFF_RESULTS",
CUFFMERGE_RESULTS = "/home/bioinfo/ShaliniR/pipeline/CUFFMERGE_RESULTS"


) 


p = Bunch(default_parameters)


#f = open(p.CUFFMERGE_RESULTS + '/assembly_GTF_list.txt', 'w')
#for sample in p.SAMPLE_LIST:
#	f.write(p.CUFFLINKS_RESULTS + "/" + sample + "/transcripts.gtf\n")
#f.close()


def fastqc():
	for sample in p.SAMPLE_LIST:
		cmd = "fastqc -o %s %s/%s.fastq" % (p.OUT_DIR, p.IN_DIR, sample)
		print cmd
		os.system(cmd)
	return

def tophat():
        for sample in p.SAMPLE_LIST:
		cmd = "tophat %s -G %s -o %s%s %s %s%s.fastq" % (p.TOPHAT_OPTIONS, p.REF_GENES, p.OUT_DIR, sample, p.BWAINDEX, p.IN_DIR, sample)
		print cmd
                os.system(cmd)
        return

def cufflinks():
	for sample in p.SAMPLE_LIST:
                cmd = "cufflinks -g %s -b %s -o %s%s %s/%s/accepted_hits.bam" % (p.REF_GENES, p.GENOME, p.CUFFLINKS_RESULTS, sample, p.TOPHAT_RESULTS, sample)
                print cmd
                os.system(cmd)
        return

def cuffmerge():
        for sample in p.SAMPLE_LIST:
		cmd = "cuffmerge -g %s -o %s -s %s %s" % (p.REF_GENES, p.CUFFMERGE_RESULTS, p.GENOME, p.GTF_LIST)
                print cmd
                os.system(cmd)
        return

def cuffdiff_miRNA():
       for sample in p.SAMPLE_LIST:
                cmd = "cuffdiff %s -o %s -b %s -u %s/merged.gtf %s %s" % (p.CUFFDIFF_OPTIONS,p.CUFFDIFF_RESULTS,p.GENOME,p.CUFFMERGE_RESULTS,p.CUFFDIFF_INPUT_LIST_COND1,p.CUFFDIFF_INPUT_LIST_COND2)
                print cmd
                os.system(cmd)
       return

if __name__ == '__main__':
	fastqc()
	tophat()
	cufflinks()
	cuffmerge()	
	cuffdiff_miRNA()
	sys.exit(0)
