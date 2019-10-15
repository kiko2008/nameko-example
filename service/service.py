from nameko.rpc import rpc, RpcProxy


class Compute(object):
    name = "compute"
    persons = RpcProxy('persons')

    @rpc
    def compute_age(self, age):
        # pdb.set_trace()
        name = ''
        try:
            name = {6: 'Kiko',
                3: 'Marcos',
                38: 'Laura',
                29: 'Tontuso papa'}

        except Exception as e:
            print('Error peristiendo a %s' % name[age])
            raise
        else:
            self.persons.save_family(
                 name[age], age
            )
            return 'El familiar se ha guardado correctamente'