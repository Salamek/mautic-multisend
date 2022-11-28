import pathlib

spool = pathlib.Path('spool')

out_spool = pathlib.Path('./out_spool')
for message in out_spool.glob('*.message'):
    message.rename(spool.joinpath(message.name))
