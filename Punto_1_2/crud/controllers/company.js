
const Company = require('../models/company')

const faker = require('faker')

const companyGet = async (req, res) => {
    const { name='', nit='', page='1', limit=10} = req.query
    const query = {enable: true}

    const [total, company] = await Promise.all([
        Company.countDocuments(query),
        Company.find(query).skip(
            (Number(page)-1)*Number(limit)).limit(Number(limit))
    ])

    res.status(200).json(
        {
            total,
            company
        }
    )
}

const companyPost = async (req, res) => {
    const { name, nit, description } = req.body;
    const company = new Company({
        name,
        nit,
        description
    })
    await company.save()
    res.status(201).json(
        {
            msg: 'created',
            company
        }
    )
}

const companyPut = async (req, res) => {
    const { id } = req.params
    const { _id, ...others } = req.body;

    const company = await Company.findByIdAndUpdate(id, others)

    res.status(204).json(
        {
            company
        }
    )
}

const companyPatch = (req, res) => {
    const { id } = req.params
    res.status(204).json(
        {
            msg: 'patch',
            id
        }
    )
}

const companyDelete = async (req, res) => {
    const { id } = req.params
    const company = await Company.findByIdAndUpdate(
        id, {enable: false})

    res.status(204).json(
        {
            company,
            msg: 'company is '
        }
    )
}

const companyFakerPost = (req, res) =>{
    const { n } = req.body;
    for(let i=0; i <= Number(n); i++)
    {
        const company = new Company({
            name: faker.company.companyName(),
            nit: faker.finance.account(),
            description: faker.lorem.text()
        })
        company.save()
    }
    res.status(200).json({
        msg: `Creating ${n} companies`
    })

}

module.exports = {
    companyGet, companyPost, companyPut,
    companyPatch, companyDelete, companyFakerPost
}
