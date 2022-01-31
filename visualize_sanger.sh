template=SNCA.fasta
allseq=allseq.fasta
rawres=raw.txt
result=res.txt
compare=comp.fasta
bwa index $template
cat *.seq > $allseq
bwa mem $template $allseq | tail -n +3 > $rawres
cut -f1,6,10 $rawres > $result
python msa_from_bwa.py $result $compare
alv comp.fasta
