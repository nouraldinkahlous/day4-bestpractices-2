from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

ranks = rank
ranks = comm.gather(ranks, root=0)
if rank == 0:
    for i in range(size):
         ranks[i] == i 
    print('Process rank:',rank,'|','Number of ranks:',size,'|','Sum of ranks:', sum(ranks))

